This package is a support package to the [bug-algorithm-using-action-server package](https://github.com/CarmineD8/assignment_2_2023) developed by [Dr. Carmine Recchiuto](https://rubrica.unige.it/personale/UkNDWV1r). This support package is useful to set goal pose and monitoring of the states of the planner package. A brief description the planner package is given below, along with how the monitoring package can be compiled and used alongside it:

## Planner Package: Bug Algorithm Using Action Server 
[This](https://github.com/CarmineD8/assignment_2_2023) package implements the bug0 algorithm on ROS noetic. The folder structure is described as follows:

```
├── action
│   ├── Planning.action
├── config
│   ├── ...
├── launch
│   ├── assignment1.launch
│   ├── sim_w1.launch
├── scripts
│   ├── bug_as.py
│   ├── go_to_point_service.py
│   ├── wall_follow_service.py
├── urdf
│   ├── ...
└── world
│   ├── robot2_laser.gazebo
│   ├── robot2_laser.xacro
└── CMakeList.txt
└── package.xml
```
