import './App.css'
import {useEffect, useState} from 'react'
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'

// Components
import Navbar from './components/Navbar'
import SideDrawer from './components/SideDrawer'
import BackDrop from './components/Backdrop'

//screens
import HomeScreen from './screens/HomeScreen'
import ProductScreen from './screens/ProductScreen'
import CartScreen from './screens/CartScreen'
import SignUp from './screens/SignUp'
import SignIn from './screens/SignIn'
import {useDispatch} from 'react-redux'
import {fetchCart} from './redux/actions/cartActions'
import {setUserDeatils} from './redux/actions/userAction'

function App() {
  const [sideToggle, setSideToggle] = useState(false)
  // fetchCart
  const dispatch = useDispatch()
  useEffect(() => {
    dispatch(fetchCart())
    dispatch(setUserDeatils())
  }, [dispatch])

  return (
    <Router>
    <Navbar click={() => setSideToggle(true)} />
    <SideDrawer show={sideToggle} click={() => setSideToggle(false)} />
    <BackDrop show={sideToggle} click={() => setSideToggle(false)} />

    <main className="app">
      <Switch>
        <Route exact path = "/" component={HomeScreen}/>
        <Route exact path="/product/:id" component={ProductScreen} />
        <Route exact path="/signup" component={SignUp} />
        <Route exact path="/cart" component={CartScreen} />
        <Route exact path="/signin" component={SignIn} />
      </Switch>
    </main>
  </Router>
  )
}

export default App


