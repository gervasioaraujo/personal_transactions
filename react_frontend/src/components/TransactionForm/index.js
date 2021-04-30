import { useEffect, useState } from 'react';
import './styles.css';

const OPERATION_TYPES = {
  INCOME: 'INCOME',
  EXPENSE: 'EXPENSE'
}

function TransactionForm({ onClickSubmit, selectedTransaction }) {

  const [transaction, setTransaction] = useState(getCleanedTransactionObject());
  const [errorMsg, setErrorMsg] = useState('');

  useEffect(() => {
    if (selectedTransaction)
      setTransaction(selectedTransaction);
  }, [selectedTransaction]);

  function getCleanedTransactionObject() {
    return { operation_type: '', description: '', amount: '' };
  }

  function handleClickAddOrEditTransaction() {
    setErrorMsg('');
    const { operation_type, description, amount } = transaction;
    if (operation_type && description && amount) {
      onClickSubmit(transaction);
      setTransaction(getCleanedTransactionObject())
    } else setErrorMsg('Todos os campos são obrigatórios!');
  }

  function handleChangeDescription(event) {
    setErrorMsg('');
    const description = event.target.value
    setTransaction({ ...transaction, description });
  }

  function handleChangeOperationType(event) {
    setErrorMsg('');
    const operation_type = event.target.value
    if (operation_type)
      setTransaction({ ...transaction, operation_type });
  }

  function handleChangeAmount(event) {
    setErrorMsg('');
    const amount = event.target.value
    setTransaction({ ...transaction, amount });
  }

  return (

    <form id="form" onSubmit={e => e.preventDefault()}>

      {errorMsg &&
        <div class="alert alert-danger">
          <span><strong>[Erro]: </strong>{errorMsg}</span>
        </div>
      }

      <div class="form-group">
        <input
          type="text"
          class="form-control"
          placeholder="Descrição da transação"
          onChange={(e) => handleChangeDescription(e)}
          value={transaction.description}
        />
      </div>

      <div class="form-group">
        <select
          class="form-control"
          onChange={(e) => handleChangeOperationType(e)}
          value={transaction.operation_type}
        >
          <option value="" selected disabled>Escolha o tipo de operação:</option>
          <option value={OPERATION_TYPES.INCOME}>Receita</option>
          <option value={OPERATION_TYPES.EXPENSE}>Despesa</option>
        </select>
      </div>

      <div class="form-group">
        <input
          type="number"
          class="form-control"
          placeholder="R$ 0,00"
          onChange={(e) => handleChangeAmount(e)}
          value={transaction.amount}
        />
      </div>

      <button class="btn btn-primary btn-block" onClick={() => {
        handleClickAddOrEditTransaction()
      }}
      >
        {selectedTransaction ? 'Editar' : 'Adicionar'}
      </button>
    </form>

  );

}

export default TransactionForm;
