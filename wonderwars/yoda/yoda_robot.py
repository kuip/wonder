import time
from WonderPy.components.wwMedia import WWMedia
from wonderwars.robot import RobotConnection


class YodaRobot(RobotConnection):
    def appearance(self, robot):
        robot.commands.RGB.stage_front(0, 0, 0)
        robot.commands.RGB.stage_ear_left(0, 0, 0)
        robot.commands.RGB.stage_ear_right(0, 0, 0)
        robot.commands.eyering.stage_eyering((False, False, True, False, False, False, False, False, False, False, True, False), 0.4)

        for i in range(1,4):
            robot.commands.head.stage_tilt_angle(-15)
            robot.commands.head.stage_tilt_angle(15)

    def presents(self, robot):
        self.appearance(robot)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_05)

        # 4 ture
        for i in range(1,6):
            robot.commands.body.stage_wheel_speeds (-7.8, 7.8)

    def wins(self, robot):
        self.appearance(robot)

        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_05)
        robot.commands.body.stage_wheel_speeds  (-35, 35)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_05)
        robot.commands.body.stage_wheel_speeds  (35, -35)

    def loses(self, robot):
        self.appearance(robot)
        robot.commands.head.stage_tilt_angle(-15)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_07)

    def rock(self, robot):
        self.appearance(robot)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_02)

    def paper(self, robot):
        self.appearance(robot)
        robot.cmds.media.stage_audio(WWMedia.WWSound.WWSoundDash.CUSTOM_03)
