"""Constants for the Smart Irrigation integration."""

DOMAIN = "smart_irrigation"
NAME = "Smart Irrigation"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.2"

ISSUE_URL = "https://github.com/jeroenterheerdt/HASmartIrrigation/issues"

# Icons
ICON = "mdi:sprinkler"

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]

# Configuration and options
CONF_API_KEY = "api_key"
CONF_REFERENCE_ET = "reference_et"
CONF_REFERENCE_ET_1 = "reference_et_1"
CONF_REFERENCE_ET_2 = "reference_et_2"
CONF_REFERENCE_ET_3 = "reference_et_3"
CONF_REFERENCE_ET_4 = "reference_et_4"
CONF_REFERENCE_ET_5 = "reference_et_5"
CONF_REFERENCE_ET_6 = "reference_et_6"
CONF_REFERENCE_ET_7 = "reference_et_7"
CONF_REFERENCE_ET_8 = "reference_et_8"
CONF_REFERENCE_ET_9 = "reference_et_9"
CONF_REFERENCE_ET_10 = "reference_et_10"
CONF_REFERENCE_ET_11 = "reference_et_11"
CONF_REFERENCE_ET_12 = "reference_et_12"
CONF_NUMBER_OF_SPRINKLERS = "number_of_sprinklers"
CONF_FLOW = "flow"
CONF_AREA = "area"
CONF_THROUGHPUT = "throughput"
CONF_PEAK_ET = "peak_et"
CONF_SYSTEM_OF_MEASUREMENT = "system_of_measurement"
CONF_PRECIPITATION_RATE = "precipitation_rate"
CONF_RAIN = "rain"
CONF_SNOW = "snow"
CONF_PRECIPITATION = "precipitation"
CONF_EVAPOTRANSPIRATION = "evapotranspiration"
CONF_WATER_BUDGET = "water_budget"
CONF_BUCKET = "bucket"
CONF_NETTO_PRECIPITATION = "netto_precipitation"

# Events
EVENT_BUCKET_UPDATED = "smart_irrigation_bucket_updated_event"

# Services
SERVICE_RESET_BUCKET = "reset_bucket"

# Systems of measurement
SETTING_METRIC = "metric"
SETTING_US = "us"

# METRIC TO IMPERIAL (US) FACTORS
MM_TO_INCH_FACTOR = 0.03937008
LITER_TO_GALLON_FACTOR = 0.26417205
M2_TO_SQ_FT_FACTOR = 10.7639104
M_TO_FT_FACTOR = 3.2808399

# Defaults
DEFAULT_NAME = NAME

# Types
TYPE_PRECIPITATION = "Precipitation"
TYPE_RAIN = "Rain"
TYPE_SNOW = "Snow"
TYPE_THROUGHPUT = "Throughput"
TYPE_PEAK_ET = "Peak Evapotranspiration"
TYPE_PRECIPITATION_RATE = TYPE_PRECIPITATION + " Rate"
TYPE_BASE_SCHEDULE_INDEX = "Base Schedule Index"
TYPE_EVAPOTRANSPIRATION = "Evapotranspiration"
TYPE_ADJUSTED_RUN_TIME = "Daily Adjusted Run Time"
TYPE_CURRENT_ADJUSTED_RUN_TIME = "Hourly Adjusted Run Time"

# UNITS
UNIT_OF_MEASUREMENT_SECONDS = "s"
UNIT_OF_MEASUREMENT_UNKNOWN = "unknown"
UNIT_OF_MEASUREMENT_LITERS = "l"
UNIT_OF_MEASUREMENT_GALLONS = "gallon"
UNIT_OF_MEASUREMENT_MMS = "mm"
UNIT_OF_MEASUREMENT_INCHES = "inch"
UNIT_OF_MEASUREMENT_M2 = "m2"
UNIT_OF_MEASUREMENT_SQ_FT = "sq ft"

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration! You will see warnings related to 'detected I/O inside the event loop'. This is normal and might be solved in future releases.
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""