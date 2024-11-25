from abc import ABC, abstractmethod

class IPrint(ABC):
    @staticmethod
    @abstractmethod
    def print():
        pass

class IScan(ABC):
    @staticmethod
    @abstractmethod
    def scan():
        pass


class Printer(IPrint):
    @staticmethod
    def print():
        print('Im a printer and Im printing')


class Scanner(IScan):
    @staticmethod
    def scan():
        print('Im a scanner and Im scanning')


class ScannerPrinter(IScan, IPrint):
    @staticmethod
    def scan():
        print('Im a Scanner Printer and Im Scanning')

    @staticmethod
    def print():
        print('Im a Scanner Printer and Im printing')

    @staticmethod
    def scan_and_print():
       print('Im a Scanner printer and Im printing and scanning')

class HP3250(ScannerPrinter):
    pass


printer = HP3250()

printer.scan()
printer.scan_and_print()
printer.print()
