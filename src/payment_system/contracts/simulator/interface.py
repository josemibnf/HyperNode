from src.payment_system.contracts.ethereum.deposit_contract.interface import CONTRACT, CONTRACT_HASH
from protos import celaut_pb2, gateway_pb2

CONTRACT_HASH = CONTRACT_HASH


def process_payment(amount: int, token: str, ledger: str,
                    contract_address: str) -> celaut_pb2.Service.Api.ContractLedger:
    print(f"Process simulated payment for token {token} of {amount}")
    return gateway_pb2.celaut__pb2.Service.Api.ContractLedger(
                ledger=ledger,
                contract_addr=contract_address,
                contract=CONTRACT
            )


def payment_process_validator(amount: int, token: str, ledger: str, contract_addr: str, validate_token) -> bool:
    return True
