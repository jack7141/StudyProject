import logging
import string
import random
from typing import List
from dataclasses import dataclass


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


class CustomerSupport:

    tickets: List[SupportTicket] = []

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(generate_id(), customer, issue))

    def process_tickets(self, processing_strategy: str = "fifo"):
        if len(self.tickets) == 0:
            logger.info("There are no tickets to process. Well done!")
            return

        if processing_strategy == 'fifo':
            for ticket in self.tickets:
                self.process_ticket(ticket)
        elif processing_strategy == 'filo':
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)
        elif processing_strategy == 'random':
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
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

    app.create_ticket("John Smith", "My computer makes strange sounds!")
    app.create_ticket("Linux Smith", "sounds!")
    app.create_ticket("Arjan Eggs Smith", "Pycharms")

    app.process_tickets("filo")