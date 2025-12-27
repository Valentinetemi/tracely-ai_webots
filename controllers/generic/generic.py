# test change


from controller import Robot
import math

robot = Robot()
timestep = int(robot.getBasicTimeStep())

t = 0.0

# UR5e joints
joint_names = [
    "shoulder_pan_joint", #rotate left/right
    "shoulder_lift_joint", #rotate up/down
    "elbow_joint", #bends arm
    "wrist_1_joint", #wrist up/down
    "wrist_2_joint", #wrist rotate
    "wrist_3_joint" #wrist rotate
]

joints = []

for name in joint_names:
    motor = robot.getDevice(name)
    motor.setVelocity(5.0)
    joints.append(motor)

# Simple pose
target_positions = [
    0.0,        # shoulder pan
    -1.2,       # shoulder lift
    1.6,        # elbow
    -1.2,       # wrist 1
    0.0,        # wrist 2
    0.0         # wrist 3
]

for joint, pos in zip(joints, target_positions):
    joint.setPosition(pos)

while robot.step(timestep) != -1:
    t += 0.01

    joints[1].setPosition(-1.2 + 0.3 * math.sin(t))
    joints[2].setPosition(1.6 + 0.3 * math.sin(t))
 
 
 #botle
 
 
