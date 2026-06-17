from src.core.constants import ProjectPaths
from src.utils.data_generator import DataGenerator



def capture(page, test_name: str) -> str:
    ProjectPaths.SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)


    screeshot_path = (
        ProjectPaths.SCREENSHOTS_DIR/
        f"{test_name}_{DataGenerator.timestamp()}.png"
    )

    page.screenshot(path=str(screeshot_path), full_page=True)

    return str(screeshot_path)