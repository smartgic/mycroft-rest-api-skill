"""Constants used across the skill
"""
MSG_PREFIX = "mycroft.api"
CONSTANT_MSG_TYPE = {
    "info": f"{MSG_PREFIX}.info",
    "connectivity": f"{MSG_PREFIX}.connectivity",
    "config": f"{MSG_PREFIX}.config",
    "skill_settings": f"{MSG_PREFIX}.skill_settings",
    "sleep": "recognizer_loop:sleep",
    "sleep_answer": f"{MSG_PREFIX}.sleep",
}
SKILLS_CONFIG_DIR = ".config/mycroft/skills"
TMP_DIR = "/tmp/mycroft"
SLEEP_MARK = f"{TMP_DIR}/sleep.mark"
AWAKE_MARK = f"{TMP_DIR}/awake.mark"
