import { EthProvider } from "./contexts/EthContext";
import Intro from "./components/Intro/";
import Setup from "./components/Setup";
import Demo from "./components/Demo";
import Footer from "./components/Footer";
import "./App.css";
import NavbarNew from "./components/frontend/Navbar";
import ContractBtns from "./components/addTransaction"
function App() {
  return (
    <EthProvider>
      <div id="App" >
        
          <NavbarNew/>
          <ContractBtns/>
        
      </div>
    </EthProvider>
  );
}
export default App;
