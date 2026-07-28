"""
Bank Account — Exercism Python Track

A simple bank account class supporting open/close, deposit, and withdrawal.

State machine
-------------
An account has two states: OPEN and CLOSED.
    • Only an OPEN account can be queried (get_balance) or modified
      (deposit, withdraw).
    • Only a CLOSED account can be opened.
    • Opening an already-open account is an error.
    • Any operation on a closed account is an error.

Validation rules
----------------
    • deposit(amount):  amount must be strictly > 0.
    • withdraw(amount): amount must be strictly > 0,
                        and amount must be <= current balance.

Exception messages (exact text required by tests)
-------------------------------------------------
    "account not open"        — operation on a closed account
    "account already open"    — open() on an already open account
    "amount must be greater than 0"  — non-positive deposit/withdraw
    "amount must be less than balance" — overdraft attempt
"""


class BankAccount:
    """A bank account with open/close lifecycle and basic transactions."""

    def __init__(self):
        """Create a new bank account in the CLOSED state with zero balance.

        The account does not exist from a banking perspective until open()
        is called.  Until then all operations except open() itself will
        raise ValueError.
        """
        # _open tracks whether the account is currently active.
        # We use a leading underscore to signal that this is internal state.
        self._open = False

        # _balance holds the current monetary balance.
        # It is only meaningful while _open is True.
        self._balance = 0

    # -----------------------------------------------------------------------
    # Helper: guard against operations on a closed account.
    # -----------------------------------------------------------------------
    def _ensure_open(self):
        """Raise ValueError if the account is not currently open."""
        if not self._open:
            raise ValueError('account not open')

    # -----------------------------------------------------------------------
    # Helper: guard against opening an already-open account.
    # -----------------------------------------------------------------------
    def _ensure_closed(self):
        """Raise ValueError if the account is already open."""
        if self._open:
            raise ValueError('account already open')

    # -----------------------------------------------------------------------
    # Public API
    # -----------------------------------------------------------------------

    def get_balance(self):
        """Return the current balance of the account.

        Raises:
            ValueError: If the account is closed.
        """
        self._ensure_open()
        return self._balance

    def open(self):
        """Open the account, resetting the balance to zero.

        An account must be closed before it can be opened.
        Re-opening an already-open account is an error.

        Raises:
            ValueError: If the account is already open.
        """
        self._ensure_closed()
        self._open = True
        self._balance = 0

    def deposit(self, amount):
        """Deposit money into the account.

        Args:
            amount (int | float): The amount to deposit. Must be > 0.

        Raises:
            ValueError: If the account is closed, or amount <= 0.
        """
        self._ensure_open()

        # The exercise requires a strictly positive amount.
        if amount <= 0:
            raise ValueError('amount must be greater than 0')

        self._balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account.

        Args:
            amount (int | float): The amount to withdraw. Must be > 0
                and must not exceed the current balance.

        Raises:
            ValueError: If the account is closed, amount <= 0,
                        or amount exceeds the balance.
        """
        self._ensure_open()

        # Same positivity check as deposit.
        if amount <= 0:
            raise ValueError('amount must be greater than 0')

        # Prevent overdraft: the account does not support negative balances.
        if amount > self._balance:
            raise ValueError('amount must be less than balance')

        self._balance -= amount

    def close(self):
        """Close the account.

        After closing, the balance is no longer accessible and the account
        must be re-opened before further use.

        Raises:
            ValueError: If the account is already closed.
        """
        self._ensure_open()
        self._open = False
        self._balance = 0