import React, { useState } from 'react';

export default function Calculator() {
  const [displayMemory, setDisplayMemory] = useState(0);
  const [displayContent, setDisplayContent] = useState(0);
  const [lastOperation, setLastOperation] = useState('');

  function prepareCalculationFor(operation){
    setLastOperation(operation);
    setDisplayMemory(displayContent);
    setDisplayContent(0);
  }

  /**
     * From stackoverflow.
     * @param {*} n 
     */
  function protectFromZeroDivision(n){
    n = +n;
    if (!n) showNotAllowedOperationMessage();
    return n;
  }


  function finishCalculationToBegin(nextOperation){
    let result = displayMemory;
    switch (lastOperation) {
      case "+": result += displayContent; break;
      case "-": result -= displayContent; break;
      case "X": result *= displayContent; break;
      case "/": result /= protectFromZeroDivision(displayContent); break;
      default: break;
    }
    setDisplayContent(result);
    setDisplayMemory(result);
    setLastOperation(nextOperation);
  }

  function showNotAllowedOperationMessage(){
    setDisplayContent("Not allowed!");
  }

  function prepareDisplay(){
    setDisplayContent("0");
  }
  
  function clear(){
    setDisplayMemory(0);
    setLastOperation("");
    setDisplayContent("0");
  }

  function handleNumericClick(value){
    setDisplayContent(prevContent => Number(`${prevContent}${value}`));
  }

  function handleOperationClick(value){
    switch (value) {
      case "C":
        clear();
        break;
      case "=":
        finishCalculationToBegin(lastOperation);
        break;
      default:
        prepareCalculationFor(value);
        break;
    }
  }

  return (
    <table>
    <tbody>
      <tr>
        <Display value={displayContent} />
      </tr>
      <tr>
        <td><NumberKey value="9" onClick={() => handleNumericClick(9)} /></td>
        <td><NumberKey value="8" onClick={() => handleNumericClick(8)} /></td>
        <td><NumberKey value="7" onClick={() => handleNumericClick(7)} /></td>
        <td><OperationKey value="+" onClick={() => handleOperationClick("+")} /></td>
      </tr>
      <tr>
        <td><NumberKey value="6" onClick={() => handleNumericClick(6)} /></td>
        <td><NumberKey value="5" onClick={() => handleNumericClick(5)} /></td>
        <td><NumberKey value="4" onClick={() => handleNumericClick(4)} /></td>
        <td><OperationKey value="-" onClick={() => handleOperationClick("-")} /></td>
      </tr>
      <tr>
        <td><NumberKey value="3" onClick={() => handleNumericClick(3)} /></td>
        <td><NumberKey value="2" onClick={() => handleNumericClick(2)} /></td>
        <td><NumberKey value="1" onClick={() => handleNumericClick(1)} /></td>
        <td><OperationKey value="X" onClick={() => handleOperationClick("X")} /></td>
      </tr>
      <tr>
        <td><NumberKey value="0" onClick={() => handleNumericClick(0)} /></td>
        <td><NumberKey value="." onClick={() => handleNumericClick(".")} /></td>
        <td></td>
        <td colSpan="2"><OperationKey value="/" onClick={() => handleOperationClick("/")} /></td>
      </tr>
      <tr>
        <td colSpan="2"><BottomKey value="C" onClick={clear} /></td>
        <td colSpan="2"><BottomKey value="=" onClick={() => handleOperationClick("=")} /></td>
      </tr>
    </tbody>
  </table>
  ); 
}

function Display({value}){return (<td colspan="4"><div className="display">{value}</div></td>);}

function NumberKey({value, onClick}){
  return (
  <button 
  className="number-key"
  onClick={onClick}
  >
    {value}
  </button>
);
}

function OperationKey({value, onClick}){
  return (
  <button 
  className="operation-key"
  onClick={onClick}>
    {value}
  </button>
  );
}

function BottomKey({value, onClick}){
  return (
  <button 
  className="bottom-key"
  onClick={onClick}>
    {value}
  </button>
  );
}