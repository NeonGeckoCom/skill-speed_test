# NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
#
# Copyright 2008-2021 Neongecko.com Inc. | All Rights Reserved
#
# Notice of License - Duplicating this Notice of License near the start of any file containing
# a derivative of this software is a condition of license for this software.
# Friendly Licensing:
# No charge, open source royalty free use of the Neon AI software source and object is offered for
# educational users, noncommercial enthusiasts, Public Benefit Corporations (and LLCs) and
# Social Purpose Corporations (and LLCs). Developers can contact developers@neon.ai
# For commercial licensing, distribution of derivative works or redistribution please contact licenses@neon.ai
# Distributed on an "AS IS” basis without warranties or conditions of any kind, either express or implied.
# Trademarks of Neongecko: Neon AI(TM), Neon Assist (TM), Neon Communicator(TM), Klat(TM)
# Authors: Guy Daniels, Daniel McKnight, Regina Bloomstine, Elon Gasper, Richard Leeds
#
# Specialized conversational reconveyance options from Conversation Processing Intelligence Corp.
# US Patents 2008-2021: US7424516, US20140161250, US20140177813, US8638908, US8068604, US8553852, US10530923, US10530924
# China Patent: CN102017585  -  Europe Patent: EU2156652  -  Patents Pending

# import subprocess
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import LOG
from adapt.intent import IntentBuilder
import speedtest
from neon_utils import stub_missing_parameters, skill_needs_patching


class SpeedTestSkill(MycroftSkill):
    def __init__(self):
        super(SpeedTestSkill, self).__init__(name="SpeedTestSkill")
        if skill_needs_patching(self):
            LOG.warning("Patching Neon skill for non-neon core")
            stub_missing_parameters(self)

    def initialize(self):
        run_test_intent = IntentBuilder("runSpeedTestIntent").require("RunSpeedTest").build()
        self.register_intent(run_test_intent, self.run_speed_test)

    def run_speed_test(self, message):
        self.speak("Starting a speed test.")
        test = speedtest.Speedtest()
        test.get_best_server()
        test.download()
        test.upload()
        res = test.results.dict()
        down = round(res['download']/1000000)
        up = round(res['upload']/1000000)
        ping = round(res['ping'])
        LOG.debug(res)
        self.speak_dialog("Results", {'down': down, 'up': up, 'ping': ping})

    def stop(self):
        pass


def create_skill():
    return SpeedTestSkill()
