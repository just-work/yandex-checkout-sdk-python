from yandex_checkout.domain.common.payment_method_type import PaymentMethodType
from yandex_checkout.domain.models.payment_data.payment_data import PaymentData


class PaymentDataAlfabank(PaymentData):
    __login = None

    def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        super(PaymentDataAlfabank, self).__init__(*args, **kwargs)
        if self.type is None or self.type is not PaymentMethodType.ALFABANK:
            self.type = PaymentMethodType.ALFABANK

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        self.__login = str(value)