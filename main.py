from services.reservation_service import BusReservationService
from ui.menu import run_menu


def main():
    service = BusReservationService()
    run_menu(service)


if __name__ == "__main__":
    main()