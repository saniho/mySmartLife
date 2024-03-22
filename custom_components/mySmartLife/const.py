""" Constants """

try:
    from homeassistant.const import Platform
except:
    pass
ISSUE_URL="https://github.com/saniho/mySmartLife/issues"

DOMAIN = "mySmartLife"

__VERSION__ = "1.0.5"

__name__ = "mySmartLife"


# Configuration
CONF_ID = "ACCESS_ID"
CONF_KEY = "ACCESS_KEY"
CONF_ENDPOINTKEY = "MQ_ENDPOINT"


try:
    PLATFORMS: list[Platform] = [Platform.SENSOR]
except:
    PLATFORMS: list = []