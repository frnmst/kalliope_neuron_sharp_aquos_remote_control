# sharp_aquos_remote_control

## Synopsis

Execute vocal commands on certain models of Sharp Aquos televisions.

## Installation

    kalliope install --git-url https://github.com/frnmst/kalliope_neuron_sharp_aquos_remote_control.git

## Options

| Parameter     | Required | Default | Choices                   | Python data type |
|-------------- |----------|---------|---------------------------|------------------|
| action        | yes      |         | <See the next table>      |   str
| command_map   | yes      | 'us'    | 'eu', 'us', 'jp', 'cn'    |   str
| ip_address    | yes      |         |                           |   str
| port          | yes      |         |                           |   int
| username      | yes      |         |                           |   str
| password      | yes      |         |                           |   str
| query         | depends  |         |                           |   str
| file_template | no       |         |                           |   str

### Actions

| Actions                | Description                                      | Query parameter required | Query parameter example        |
|------------------------|--------------------------------------------------|---------------------|---------------------------|
| on                     | power on the television                          |   no                |                           |
| off                    | power off the television                         |   no                |                           |
| status                 | check the status of the television               |   no                |                           |
| volume                 | set volume to the specified value                |   yes               | '10'                      |
| mute_toggle            | toggle mute                                      |   no                |                           |
| digital_channel_cable  | change channel to the specified value            |   yes               | '50'                      |
| teletext_toggle        | enable the teletext                              |   no                |                           |
| teletext_jump          | jump to the specified teletext page              |   yes               | '103'                     |
| input                  | change to the specified source                   |   yes               | "hdmi 1"                  |
| sleep                  | set the standby timer for the specified minutes  |   yes               | "30", use "0" to disable  | 
| remote_button_seq      | imitate the pressing of buttons on the remote    |   yes               | "['menu','left','enter']" |

| Query parameters accepted values    |
|-------------------------------------|
| '0' <= volume <= '60'               |
| 1 <= digital_channel_cable <= '999' |
| '100' <= teletext_jump <= 899       |
| input =  see the [python API](https://github.com/sharp-aquos-remote-control/sharp_aquos_rc/blob/master/sharp_aquos_rc/commands/eu.yaml) , the `input` section.   |
| sleep = {0,30,60,90,120}          |
| remote_button_seq = see [python API](https://github.com/sharp-aquos-remote-control/blob/master/sharp_aquos_rc/commands/eu.yaml) , the `remote` section. |

## Return Values

| Name               | Description         | Python data type | Return codes |
---------------------|---------------------|------------------|--------------|
| powerstatus        | Tells respectively if the tv is unreachable, turned off or powered on | int | -1, 0, 1 |
| actionsuccessful   | Tells if the last action was successful. This is not available for the tv_status action | boolean | True, False |

## Python API

See the [original](https://github.com/jmoore987/sharp_aquos_rc) and a
[more updated version](https://github.com/frnmst/sharp_aquos_rc)
of the underlying python API.

## Synapses and templates example

Have a look at the `./brain.yml` and `./template.j2` files

## TODO

- Try what happens if i say: "Television channel" (ie when channel, volume, etc...
  is not specified).
- Fix documentation
- Multi language templates
- How to specify automatically when to use
  digital_channel_cable or digital_channel_air
- Finish all the commands
- Fix neuron controls
- Add neuron tests (and find a way to run them the "correct" way).
- Test installation
- General cleaning

## Copyright and License

Copyright (c) 2017, Franco Masotti

Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
SOFTWARE.

