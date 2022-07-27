import './App.css'
import {useEffect, useState} from 'react'
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'

// Components
import Navbar from './components/Navbar'


function App() {
  const [sideToggle, setSideToggle] = useState(false)
  return (
    <Router>
      <Navbar click={() => setSideToggle(true)} />
    </Router>
  )
}

export default App


