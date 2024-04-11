import traceback
from enum import Enum, unique
from typing import List, Optional


@unique
class Channel(Enum):
    DOUBLE_GIS = '2gis'
    # Deprecated. Use USER_ID
    APPLICATION = 'app'
    APPSTORE = 'as'
    EMAIL = 'em'
    FACEBOOK = 'fb'
    USER_ID = 'id'
    INSTAGRAM = 'ig'
    GOOGLE_PLAY = 'gp'
    SIP = 'sip'
    SMS = 'sms'
    TELEGRAM = 'tg'
    TWITTER = 'tw'
    VIBER = 'vb'
    VKONTAKTE = 'vk'
    WEB_PARSER = 'wp'
    WHATSAPP = 'wpp'
    WEBSOCKET = 'ws'
    YOUTUBE = 'yt'

    @staticmethod
    def of(value) -> Optional['Channel']:
        if not value:
            return None
        try:
            channel = Channel(value)
        except (Exception,):
            traceback.print_exc()
            return None

        if channel.is_application:  # Compatibility with older versions
            return Channel.USER_ID

        return channel

    @staticmethod
    def values() -> List[str]:
        return [c.value for c in Channel]

    @staticmethod
    def items() -> list:
        return [c.to_dict() for c in Channel]
        # channels = []
        # for c in Channel:
        #     if c in [Channel.APPLICATION, Channel.INSTAGRAM]:
        #         continue
        #     channels.append(c.to_dict())
        # return channels

    def to_dict(self) -> dict:
        return {
            'key': self.value,
            'display_name': self.display_name,
        }

    @property
    def is_application(self) -> bool:
        return self == Channel.APPLICATION

    @property
    def is_appstore(self) -> bool:
        return self == Channel.APPSTORE

    @property
    def is_email(self) -> bool:
        return self == Channel.EMAIL

    @property
    def is_facebook(self) -> bool:
        return self == Channel.FACEBOOK

    @property
    def is_instagram(self) -> bool:
        return self == Channel.INSTAGRAM

    @property
    def is_google_play(self) -> bool:
        return self == Channel.GOOGLE_PLAY

    @property
    def is_mobile_application(self) -> bool:
        return self.is_application or self.is_user_id

    @property
    def is_sip(self) -> bool:
        return self == Channel.SIP

    @property
    def is_sms(self) -> bool:
        return self == Channel.SMS

    @property
    def is_telegram(self) -> bool:
        return self == Channel.TELEGRAM

    @property
    def is_twitter(self) -> bool:
        return self == Channel.TWITTER

    @property
    def is_user_id(self) -> bool:
        return self == Channel.USER_ID

    @property
    def is_viber(self) -> bool:
        return self == Channel.VIBER

    @property
    def is_vkontakte(self) -> bool:
        return self == Channel.VKONTAKTE

    @property
    def is_whatsapp(self) -> bool:
        return self == Channel.WHATSAPP

    @property
    def is_websocket(self) -> bool:
        return self == Channel.WEBSOCKET

    @property
    def is_youtube(self) -> bool:
        return self == Channel.YOUTUBE

    @property
    def is_web_parser(self) -> bool:
        return self == Channel.WEB_PARSER

    @property
    def is_2gis(self) -> bool:
        return self == Channel.DOUBLE_GIS

    @property
    def display_name(self) -> Optional[str]:
        if self.is_mobile_application:
            return 'Мобильное приложение'
        elif self.is_appstore:
            return 'App Store'
        elif self.is_email:
            return 'Электронная почта'
        elif self.is_facebook:
            return 'Facebook'
        elif self.is_instagram:
            return 'Instagram'
        elif self.is_google_play:
            return 'Google Play'
        elif self.is_sip:
            return 'Телефония'
        elif self.is_sms:
            return 'SMS'
        elif self.is_telegram:
            return 'Telegram'
        elif self.is_twitter:
            return 'Twitter'
        elif self.is_viber:
            return 'Viber'
        elif self.is_vkontakte:
            return 'ВКонтакте'
        elif self.is_whatsapp:
            return 'WhatsApp'
        elif self.is_websocket:
            return 'Веб-виджет'
        elif self.is_youtube:
            return 'YouTube'
        elif self.is_web_parser:
            return 'Веб-парсер'
        elif self.is_2gis:
            return '2GIS'
        return None

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == other
        elif isinstance(other, Channel):
            return self.value == other.value
        return False
