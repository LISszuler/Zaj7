from src.models import Parameters, Transfer
from src.manager import Manager


def test_validate_transfers_reports_unknown_tenant():
    manager = Manager(Parameters())
    manager.transfers.append(Transfer(
        tenant='tenant-999',
        date='2024-06-01',
        settlement_year=2024,
        settlement_month=6,
        amount_pln=1000.0,
        type='payment'
    ))

    errors = manager.validate_transfers()

    assert isinstance(errors, list)
    assert len(errors) == 1
    assert 'unknown tenant' in errors[0].lower()


def test_validate_transfers_reports_transfer_outside_tenant_agreement():
    manager = Manager(Parameters())
    manager.transfers.append(Transfer(
        tenant='tenant-1',
        date='2025-01-01',
        settlement_year=2025,
        settlement_month=1,
        amount_pln=1500.0,
        type='payment'
    ))

    errors = manager.validate_transfers()

    assert isinstance(errors, list)
    assert len(errors) == 1
    assert 'outside agreement' in errors[0].lower()


def test_validate_transfers_returns_no_errors_for_valid_transfer():
    manager = Manager(Parameters())
    manager.transfers.append(Transfer(
        tenant='tenant-1',
        date='2024-06-01',
        settlement_year=2024,
        settlement_month=6,
        amount_pln=1500.0,
        type='payment'
    ))

    errors = manager.validate_transfers()

    assert errors == []
