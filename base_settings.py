# Settings for the citation extractor

# Sets debug on (=true) or off (=false)
DEBUG = False

# leave empty to write the log to the console
LOG_FILE = ""

# list of directories containing data (IOB format with .iob extension)
DATA_DIRS = (
	"data/",
	"data_C1/",
)

DATA_FILE = "data/test.txt"

OUTPUT_DIR = "out/"

# number of iterations for the k-fold cross validation
CROSS_VAL_FOLDS = 10

CRFPP_TEMPLATE_DIR = "crfpp_templates/"

CRFPP_TEMPLATE = "baseline.tpl"

# Leave empty to use CRF++'s default value
CRFPP_PARAM_C = ''

# Leave empty to use CRF++'s default value
CRFPP_PARAM_A = ''

# Leave empty to use CRF++'s default value
CRFPP_PARAM_F = ''