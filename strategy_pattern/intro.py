import logging
import string
import random
from typing import List
from dataclasses import dataclass
from abc import ABC, abstractmethod

logger = logging.getLogger()


def generate_id(length=8):
    """자동차 번호를 난수의 알바벳으로 생성합니다.

    example

    >>> HWKQNMVHCOHA

    """
    return ''.join(random.choices(string.ascii_uppercase, k=length))


@dataclass
class SupportTicket:
    id: str
    customer: str
    issue: str


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()


class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy


class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy


class BlackHoleOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return []


class CustomerSupport:

    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(generate_id(), customer, issue))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        ticket_list = processing_strategy.create_ordering(self.tickets)

        if len(self.tickets) == 0:
            logger.info("There are no tickets to process. Well done!")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)


    def process_ticket(self, ticket: SupportTicket):
        logger.info("===========================================")
        logger.info(f"Processing ticket id: {ticket.id}")
        logger.info(f"Customer: {ticket.customer}")
        logger.info(f"Issue: {ticket.issue}")
        logger.info("===========================================")

if __name__ == '__main__':
    logging.basicConfig(format='[%(asctime)s-%(levelname)s] %(message)s',
                        level=logging.INFO)

    app = CustomerSupport()

    app.create_ticket("1", "My computer makes strange sounds!")
    app.create_ticket("2", "sounds!")
    app.create_ticket("3", "Pycharms")

    app.process_tickets(FILOOrderingStrategy())