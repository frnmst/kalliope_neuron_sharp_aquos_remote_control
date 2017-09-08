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

                if self.configuration['action'] == "tv_on":
                    logger.debug("Sharp TV Action: tv_on")
                    success = self.sharp_tv_action_on()

                elif self.configuration['action'] == "tv_off":
                    logger.debug("Sharp TV Action: tv_off")
                    success = self.sharp_tv_action_off()

                elif self.configuration['action'] == "tv_status":
                    logger.debug("Sharp TV Action: tv_status")
                    power_status = self.sharp_tv_action_status()

                elif self.configuration['action'] == "tv_volume":
                    logger.debug("Sharp TV Action: tv_volume")
                    success = self.sharp_tv_action_volume()

                elif self.configuration['action'] == "tv_digital_channel_cable":
                    logger.debug("Sharp TV Action: tv_digital_channel_cable")
                    success = self.sharp_tv_action_digital_channel_cable()

                elif self.configuration['action'] == "tv_mute_toggle":
                    logger.debug("Sharp TV Action: tv_mute_toggle")
                    success = self.sharp_tv_action_mute_toggle()

                else:
                    logger.debug("Sharp TV Action: Not found")

            except Exception as e:
                # Television is offline.
                success = False
                if self.configuration['action'] ==  "tv_status":
                    power_status = -1
                    success = None
                logger.debug(e)
        else:
            status = "...Param error..."

        message = {
            'actionsuccessful': success,
            'powerstatus': power_status
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

    def sharp_tv_action_mute_toggle(self):

        results = self.client.mute(0)

        return results

    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise
        .. raises:: InvalidParameterException
        """

        if self.configuration['ip_address'] is None:
            raise InvalidParameterException("Sharp Aquos Remote needs an ip address")
        if self.configuration['port'] is None:
            raise InvalidParameterException("Sharp Aquos Remote needs a port")

        if self.configuration['action'] is None:
            raise InvalidParameterException("Invaliad action")

        elif (self.configuration['action'] in ['tv_volume', 'tv_digital_channel_cable']
            and self.configuration['query'] is None):
            raise InvalidParameterException("Sharp Aquos Remote requires a query for this action")

#        if (self.configuration['action'] in ['mute']
#            and self.configuration['query'] not in [0, 1, 2]):
#            raise InvalidParameterException("Sharp Aquos Remote requires a value of 0, 1 or 2 for this action")

        return True
