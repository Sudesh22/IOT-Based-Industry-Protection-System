import './App.css';
import React from 'react';
import Signin from './Components/Signin/Signin';
import Signup from './Components/Signup/Signup';
import Particle from './Components/Particles/Particles';

export default function App() {
  const [state, setState] = React.useState({
    route: 'signin',
    isSignedin: false
  })
  function onRouteChange(route) {
    setState(prev => ({ ...prev, route: route }))
  }

  return (
    <div className='landUpPage'>
      <Particle />
      <div className='titles'>
        <h1>Industry</h1>
        <p>Your life is under Our Security......</p>
      </div>
      <div className='container'>
        {state.route === 'signin' ?
          <Signin onRouteChange={onRouteChange} />
          :
          <Signup onRouteChange={onRouteChange} />}
      </div>
    </div>

  );
}