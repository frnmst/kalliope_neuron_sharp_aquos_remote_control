# sharp_aquos_remote_control.py
#
# Copyright (c) 2017, Franco Masotti
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging

from kalliope.core.NeuronModule import NeuronModule, InvalidParameterException
import sharp_aquos_rc

logging.basicConfig()
logger = logging.getLogger("kalliope")


class Sharp_aquos_remote_control(NeuronModule):
    # Pass a variable number of arguments to this method (see kwargs).
    # It's like argv in C. It means keyworded.
    def __init__(self, **kwargs):
        super(Sharp_aquos_remote_control, self).__init__(**kwargs)

        # get parameters form the neuron
        self.configuration = {
            "action": kwargs.get('action', None),
            "command_map": kwargs.get('command_map', 'eu'),
            "ip_address": kwargs.get('ip_address', None),
            "port": kwargs.get('port', 10002),
            "username": kwargs.get('username', 'admin'),
            "password": kwargs.get('password', 'password'),
            "query": kwargs.get('query', None)
        }


        self.init_sharp_tv_client()

        power_status = None
        success = None

        # check parameters
        if self._is_parameters_ok():
            try:
                if self.configuration['action'] == "on":
                    logger.debug("Sharp TV Action: on")
                    success = self.sharp_tv_action_on()

                elif self.configuration['action'] == "off":
                    logger.debug("Sharp TV Action: off")
                    success = self.sharp_tv_action_off()

                elif self.configuration['action'] == "status":
                    logger.debug("Sharp TV Action: status")
                    power_status = self.sharp_tv_action_status()

                elif self.configuration['action'] == "volume":
                    logger.debug("Sharp TV Action: volume")
                    success = self.sharp_tv_action_volume()

                elif self.configuration['action'] == "digital_channel_cable":
                    logger.debug("Sharp TV Action: digital_channel_cable")
                    success = self.sharp_tv_action_digital_channel_cable()

                elif self.configuration['action'] == "mute_toggle":
                    logger.debug("Sharp TV Action: mute_toggle")
                    success = self.sharp_tv_action_mute_toggle()

                elif self.configuration['action'] == "channel_up":
                    logger.debug("Sharp TV Action: channel_up")
                    success = self.sharp_tv_action_channel_up()

                elif self.configuration['action'] == "channel_down":
                    logger.debug("Sharp TV Action: channel_down")
                    success = self.sharp_tv_action_channel_down()

                elif self.configuration['action'] == "mute_toggle":
                    logger.debug("Sharp TV Action: mute_toggle")
                    success = self.sharp_tv_action_mute_toggle()

                elif self.configuration['action'] == "teletext_jump":
                    logger.debug("Sharp TV Action: teletext_jump")
                    success = self.sharp_tv_action_teletext_jump()

                elif self.configuration['action'] == "teletext_toggle":
                    logger.debug("Sharp TV Action: teletext_toggle")
                    success = self.sharp_tv_action_teletext_toggle()

                else:
                    logger.debug("Sharp TV Action: Not found")

            except Exception as e:
                # Television is offline. FIXME: this is ugly.
                success = False
                if self.configuration['action'] ==  "status":
                    power_status = -1
                    success = None
                logger.debug(e)
        else:
            status = "...Param error..."

        message = {
            'action_successful': success,
            'power_status': power_status
        }

        self.say(message)

    def init_sharp_tv_client(self):

        client = None

        try:
            client = sharp_aquos_rc.TV(self.configuration['ip_address'],
                                       self.configuration['port'],
                                       self.configuration['username'],
                                       self.configuration['password'],
                                       command_map=self.configuration['command_map'])
            self.client = client

        except Exception as e:
            logger.debug("error: %s" % e)
            self.client = False

    def sharp_tv_action_on(self):

        results = self.client.power(1)

        return results

    def sharp_tv_action_off(self):

        results = self.client.power(0)

        return results

    def sharp_tv_action_status(self):

        results = self.client.power()

        return results

    def sharp_tv_action_volume(self):

        results = self.client.volume(self.configuration['query'])

        return results

    def sharp_tv_action_digital_channel_cable(self):

        results = self.client.digital_channel_cable(self.configuration['query'])

        return results

    def sharp_tv_channel_up(self):

        results = self.client.channel_up()

        return results

    def sharp_tv_channel_down(self):

        results = self.client.channel_down()

        return results

    def sharp_tv_action_mute_toggle(self):

        results = self.client.mute(0)

        return results

    def sharp_tv_action_teletext_jump(self):

        # Reset status and call teletext
        results = (self.client.teletext(0) and self.client.teletext(1)
            and self.client.teletext_jump(self.configuration['query']))

        return results

    def sharp_tv_action_teletext_toggle(self):

        results = self.client.teletext(1)

        return results

    def sharp_tv_action_sleep(self):

        if self.configuration['query'] == 0:
	        results = self.client.sleep(0)
        elif self.configuration['query'] == 30:
	        results = self.client.sleep(1)
        elif self.configuration['query'] == 60:
	        results = self.client.sleep(2)
        elif self.configuration['query'] == 90:
	        results = self.client.sleep(3)
        elif self.configuration['query'] == 120:
	        results = self.client.sleep(4)

        return results

    def sharp_tv_action_remote_button_seq(self):

        results = True
        for button in self.configuration['query']:
            results = results and self.client.remote_button(button)

        return results

    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise
        .. raises:: InvalidParameterException
        """

        # Check simple parameters.
        if self.configuration['ip_address'] is None:
            raise InvalidParameterException("Sharp Aquos Remote needs an ip address")
        if self.configuration['port'] is None:
            raise InvalidParameterException("Sharp Aquos Remote needs a port")
        if self.configuration['username'] is None:
            raise InvalidParameterException("Sharp Aquos Remote needs a username")
        if self.configuration['password'] is None:
            raise InvalidParameterException("Sharp Aquos Remote needs a password")

        # Check that the query is not empty for some corresponding actions.
        if self.configuration['action'] is None:
            raise InvalidParameterException("Sharp Aquos Remote requires a valid action")
        elif self.configuration['action'] in ['volume', 'digital_channel_cable', 'teletext_jump','sleep']:
            if self.configuration['query'] is None:
                raise InvalidParameterException("Sharp Aquos Remote requires a query for this action")
        elif self.configuration['action'] in ['on','off']:
            pass
        else:
            raise InvalidParameterException("Sharp Aquos Remote requires a valid action")

        if self.configuration['action'] == 'teletext_jump':
            if self.configuration['query'] < 100 or self.configuration['query'] > 899:
                raise InvalidParameterException("Sharp Aquos Remote requires a page index between \
                                                100 and 899 to do the teletext jump")

        # Check the command map.
        if self.configuration['command_map'] is None:
            raise InvalidParameterException("Sharp Aquos Remote needs a valid command map")
        elif self.configuration['command_map'] not in ['eu','jp','us','cn']:
            raise InvalidParameterException("Sharp Aquos Remote needs a valid command map")


        # Check the sleep parameters.
        if self.configuration['action'] == 'sleep':
            if self.configuration['query'] not in ['0', '30', '60', '90', '120']:
                raise InvalidParameterException("Sharp Aquos Remote requires a valid sleep timer time.")

        return True
