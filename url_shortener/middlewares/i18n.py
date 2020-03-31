from pathlib import Path

from dataclasses import field, dataclass
from typing import Any, Tuple

from aiogram.contrib.middlewares.i18n import I18nMiddleware as BaseI18nMiddleware
from aiogram import Dispatcher


@dataclass
class LanguageData:
    flag: str
    title: str
    label: str = field(init=False, default=None)

    def __post_init__(self):
        self.label = f"{self.flag} {self.title}"


class I18nMiddleware(BaseI18nMiddleware):
    AVAILABLE_LANGUAGES = {
        'ru': LanguageData('🇷🇺', 'Русский'),
        'en': LanguageData('🇺🇸', 'English')
    }

    async def get_user_locale(self, action: str, args: Tuple[Any]) -> str:
        state = Dispatcher.get_current().current_state()
        data = await state.get_data()

        if locale := data.get('locale'):
            return locale

        return self.default


BASE_DIR = Path(__file__).parents[1]
LOCALES_DIR = BASE_DIR / 'locales'

i18n = I18nMiddleware('mybot', LOCALES_DIR)
_ = i18n.gettext
