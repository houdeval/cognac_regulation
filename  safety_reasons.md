# Reasons for the float to go to safety mode

The parameters at stake can be changed in the file safety.launch in the package seabot_safety/launch without compilation.



|Safety reasons:     |published frequency            |depth limit           |battery limit        |depressurization              |seafloor            |
| :------------      | :------------                 | :------------        | :------------       | :------------                | :------------      |
| Explanation:       |no data received from          |the float is          |low battery          |-water leak                   |-seafloor reached   |
|                    |batteries, internal sensors,   |too deep              |                     |-too high internal pressure   |                    |
|                    |external sensors,              |                      |                     |-too high variation of volume |                    |
|                    |piston sensor, euler method    |                      |                     |                              |                    |
|--------------------|-------------------------------|----------------------|---------------------|------------------------------|--------------------|
|Parameters at stake:|-time_delay_euler_msg          |-safety_pressure_limit|-safety_battery      |-humidity_limit               |max_speed_reset_zero|
|                    |-time_delay_batteries_msg      |-pressure_limit       |-battery_limit       |-pressure_internal_max        | -time_before_      |
|                    |-time_delay_internal_sensor_msg|-time_before_         |-delta_volume_allowed|                              |seafloor_emergency  |
|                    |-time_delay_external_sensor_msg|pressure_emergency    |                     |-delta_ref_allowed            |                    |
|                    |-time_delay_depth_msg          |                      |                     |-volume_ref                   |                    |
|                    |-time_delay_piston_state_msg   |                      |                     |-transition_tick_law          |                    |
|                    |                               |                      |                     |-safety_depressure            |                    |
|--------------------|-------------------------------|----------------------|---------------------|------------------------------|--------------------|
|Solutions:          |-check connections             |restart mission       |charge               |-check internal pressure      |-restart mission    |
|                    |-addressing issues             |with lower depth      |batteries            |-check humidity               |with lower  depth   |
|                    |-restart mission               |                      |                     |-allow higher volume variation|-piston completely  |
|                    |                               |                      |                     |                              |held in but speed   |
|                    |                               |                      |                     |                              |is low: change      |
|                    |                               |                      |                     |                              |max_speed_reset_zero|
|--------------------|-------------------------------|----------------------|---------------------|------------------------------|--------------------|
