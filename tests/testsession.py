from sqlalchemy import event
from sqlalchemy.orm import Session, sessionmaker, scoped_session


class TestSession(Session):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.begin_nested()

        @event.listens_for(self, "after_transaction_end")
        def restart_savepoint(session, transaction):
            if transaction.nested and not transaction._parent.nested:
                session.expire_all()
                session.begin_nested()


MySession = scoped_session(sessionmaker(autoflush=False, class_=TestSession))