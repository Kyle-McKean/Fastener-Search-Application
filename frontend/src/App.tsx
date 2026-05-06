import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import FastenerSearch from './components/FastenerSearch'

function App() {

  return (
    <>
      <section id="center"> 
        <FastenerSearch />
      </section>
    </>
  )
}

export default App
