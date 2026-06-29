from dataclasses import dataclass

DEFAULT_PAGE = "landing"


@dataclass
class AppState:
    current_page: str = DEFAULT_PAGE
    previous_page: str | None = None
    loading: bool = False
    first_visit: bool = True

    def reset(self) -> None:
        self.current_page = DEFAULT_PAGE
        self.previous_page = None
        self.loading = False
        self.first_visit = True


# Estado global de la aplicación
app_state = AppState()