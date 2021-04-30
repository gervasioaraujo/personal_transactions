import { useState, useEffect } from 'react';

import TransactionForm from '../../components/TransactionForm';
import './styles.css';


function Dashboard() {

  const [transactions, setTransactions] = useState([]);
  const [selectedTransaction, setSelectedTransaction] = useState(null);

  useEffect(() => {
    const URL = 'http://localhost:8000/api/transactions/';
    fetch(URL)
      .then(response => response.json())
      .then(data => {
        setTransactions(data);
      });
  }, [])

  const createOrUpdateTransaction = (transactionData) => {

    let url = '';
    let method = '';

    if (transactionData.id) {
      url = `http://localhost:8000/api/transactions/${transactionData.id}/update`;
      method = 'PUT';
    } else {
      url = 'http://localhost:8000/api/transactions/create';
      method = 'POST';
    }

    const requestOptions = {
      method: method,
      body: JSON.stringify(transactionData),
      headers: new Headers({
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }),
    };
    fetch(url, requestOptions)
      .then(response => response.json())
      .then(data => {
        if (transactionData.id) {
          const updatedList = transactions.map(t => t.id === data.id ? data : t);
          setTransactions(updatedList);
        } else setTransactions([data, ...transactions]);
      });
  }

  function selectTransaction(transactionId) {
    const transaction = transactions.find(t => t.id === transactionId);
    setSelectedTransaction(transaction);
  }

  function deleteTransaction(transactionId) {
    const URL = `http://localhost:8000/api/transactions/${transactionId}/delete`;
    const requestOptions = {
      method: 'DELETE',
    };
    fetch(URL, requestOptions)
      .then(response => {
        // console.log(response);
        if (response.status === 204) {
          const newTransactionsList = transactions.filter(transaction => transaction.id !== transactionId);
          setTransactions(newTransactionsList);
        }
      });
  }

  function renderBalance() {
    const balance = transactions.reduce(function (total, transaction) {
      const amount = transaction.operation_type === 'INCOME' ? parseFloat(transaction.amount) : parseFloat(transaction.amount) * -1
      return total + amount;
    }, 0);
    return <h1 id="balance" class="balance">R$ {balance}</h1>;
  }

  function renderIncomes() {
    const incomes = transactions.reduce(function (total, transaction) {
      const amount = transaction.operation_type === 'INCOME' ? parseFloat(transaction.amount) : 0
      return total + amount;
    }, 0);
    return <p id="money-plus" class="money plus">+ R$ {incomes}</p>;
  }

  function renderExpenses() {
    const expenses = transactions.reduce(function (total, transaction) {
      const amount = transaction.operation_type === 'EXPENSE' ? parseFloat(transaction.amount) : 0
      return total + amount;
    }, 0);
    return <p id="money-minus" class="money minus">- R$ {expenses}</p>;
  }

  function renderTransactions() {
    return transactions.map(transaction => {

      const { id, description, amount, operation_type, created_at } = transaction;
      const formatted_amount = operation_type === 'INCOME' ? `R$ ${amount}` : `- R$ ${amount}`;

      return <tr key={id} class={operation_type === 'INCOME' ? "plus" : "minus"}>
        <td class="description">
          <span>{description}</span> <br />
          <small>{new Date(created_at).toLocaleDateString()}</small>
        </td>
        <td class="amount">
          <span class={operation_type === 'INCOME' ? "money plus" : "money minus"}>
            {formatted_amount}
          </span>
        </td>
        <td class="btn-actions">
          <button class="btn btn-sm" onClick={() => selectTransaction(id)}>
            <i class="fa fa-pencil"></i>
          </button>
          <button class="btn btn-sm" onClick={() => deleteTransaction(id)}>
            <i class="fa fa-trash"></i>
          </button>
        </td>
      </tr>;
    });
  }

  return (
    <div className="container">

      <header class="header">
        <h2>Controle Financeiro</h2>

        <h4>Saldo atual</h4>
        {renderBalance()}
      </header>

      <div class="inc-exp-container">
        <div>
          <h4>Receitas</h4>
          {renderIncomes()}
        </div>

        <div>
          <h4>Despesas</h4>
          {renderExpenses()}
        </div>
      </div>

      <div class="row">

        <div class="col-sm-6">
          <h3>Adicionar Transação</h3>
          <TransactionForm
            onClickSubmit={createOrUpdateTransaction}
            selectedTransaction={selectedTransaction}
          />
        </div>

        <div class="col-sm-6">
          <h3>Transações</h3>
          <table class="transactions table table-hover">
            <tbody>
              {renderTransactions()}
            </tbody>
          </table>
        </div>

      </div>

    </div>
  );

}

export default Dashboard;
