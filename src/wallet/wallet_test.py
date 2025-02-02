#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from wallet import wallet as w


@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''

    return w.Wallet()


@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''

    return w.Wallet(20)


def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100


def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10


def TestWalletSpendCashRaisesExceptionOnInsufficientAmount(empty_wallet):
    with pytest.raises(w.InsufficientAmount):
        empty_wallet.spend_cash(100)
