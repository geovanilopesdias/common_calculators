import React from 'react';
import ReactDOM from 'react-dom';
import Calculator from './Calculator';
import './App.css';
import './calculator.css';

export default function App() {
  return (
    <div className="App">
      <Header />
      <section id="section" class="container">
        <Calculator />
      </section>
      
    </div>
  );
}


function Header(){
  return(
    <header className='jumbotron jumbotron-fluid text-center'>
      <h1>Calculadora Simples</h1>
      <p>
        Baseada em meu pequeno (e ingênuo) 
        <a href="https://github.com/geovanilopesdias/common_calculators"> projeto em Python/Tkinter.</a>
      </p>
      <p>
        Código disponível 
        <a href="https://github.com/geovanilopesdias/common_calculators"> aqui.</a>
      </p>
    </header>
  );
}

// function Nav(){
//     function handleClickHome(){
//       ReactDOM.render(
//         <Section titulo="inicial" texto="Texto a ser exibido" />,
//         document.getElementById('section')
//       );
//     }


//   function handleClickComponents(){
//     ReactDOM.render(
//       <Section titulo="inicial" texto="Texto a ser exibido" />,
//       document.getElementById('section')
//     );
//   }

//   function handleClickProps(){
//     ReactDOM.render(
//       <Section titulo="Props" texto="Texto sobre Props" />,
//       document.getElementById('section')
//     );
//   }

//   function handleClickAlternative(){
//     ReactDOM.render(
//       <Section titulo="Componente alternativo" texto="Exemplo com outro componente" />,
//       document.getElementById('section')
//     );
//   }

//   return(
//     <nav className='navbar navbar-expand-sm bg-dark navbar-dark'>
//       <a className='navbar-brand' onClick={handleClickHome} href='#'>Home</a>
//       <button className='navbar-toggler' type='button'>
//         <span className='navbar-toggler-icon'></span>
//       </button>
//       <div className='collapse navbar-collapse'>
//         <ul className='navbar-nav'>
//         <li className='navbar-item'>
//           <a className='nav-link' onClick={handleClickComponents} href='#'> Componentes</a>
//         </li>
//         <li className='navbar-item'>
//           <a className='nav-link' onClick={handleClickProps} href='#'> Props</a>
//         </li>
//         <li className='navbar-item'>
//           <a className='nav-link' onClick={handleClickAlternative} href='#'> Outro componentes</a>
//         </li>
//         </ul>
//       </div>
//     </nav>
//   );
// }


function Section(props){
  return(
    <div className='row'>
      <div className='col-sm-6'>
      <Calculator />
    </div>
    </div>
  );
}

// function Footer(){
//   return(
//     <footer className='jumbotron text-center'>
//       <p>Footer</p>
//     </footer>
//   );
// }