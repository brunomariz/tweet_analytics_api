CYAN='\033[1;36m'
NC='\033[0m' # No Color
TRIANGLE='\xE2\x96\xB8'

echo "\n [${CYAN}👾 Running app on port ${1:-5000} ...${NC}]\n"

uvicorn src.main:app --reload --port ${1:-5000}