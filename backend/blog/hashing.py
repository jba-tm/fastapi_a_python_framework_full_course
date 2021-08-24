from passlib.context import CryptContext

__all__ = ['Hash']

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash(object):
    @staticmethod
    def bcrypt(password: str, ):
        return pwd_context.hash(password)
