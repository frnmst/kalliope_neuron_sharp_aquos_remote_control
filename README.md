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


| Actions                   | Description                               | query parm required | query parm |
|---------------------------|-------------------------------------------|---------------------|------------|
| tv_on                     | power on the television                   |   no                |            |
| tv_off                    | power off the television                  |   no                |            |
| tv_status                 | check the status of the television        |   no                |            |
| tv_volume                 | set volume to the specified value         |   yes               |            |
| tv_mute_toggle            | toggle mute                               |   no                |            |
| tv_digital_channel_cable  | change channel to the specified value     |   yes               |            |
| ... | | |

## Return Values

| Name               | Description         | Python data type | Return codes |
---------------------|---------------------|------------------|--------------|
| powerstatus        | Tells respectively if the tv is unreachable, turned off or powered on | int | -1, 0, 1 |
| actionsuccessful   | Tells if the last action was successfull. This is not available for the tv_status action | boolean | True, False |

## Python API

See the [original](https://github.com/jmoore987/sharp_aquos_rc) and a
[more updated version](https://github.com/frnmst/sharp_aquos_rc)
of the underlying python API.

## Synapses and templates example

Have a look at the `brain.yml` and `./template.j2` files

## TODO

- Fix documentation
- Multi language templates
- Define the commands better
- Finish all the commands
- Fix neuron controls
- Add neuron tests
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

