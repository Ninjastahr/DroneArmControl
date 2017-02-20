from ArmController import ArmMovement
from Constants import *

arm = ArmMovement.ArmControl()

arm.setAngle(CONST_BASE_CHANNEL, 100)
arm.setAngle(CONST_JOINT_1_CHANNEL,100)
arm.setAngle(CONST_JOINT_2_CHANNEL,50)
arm.setAngle(CONST_JOINT_3_CHANNEL,50)
arm.setAngle(CONST_GRIPPER_CHANNEL,20)