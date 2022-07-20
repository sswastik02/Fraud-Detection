import { EthProvider } from "./contexts/EthContext";
import Intro from "./components/Intro/";
import Setup from "./components/Setup";
import Demo from "./components/Demo";
import Footer from "./components/Footer";
import "./App.css";
import NavbarNew from "./components/frontend/Navbar";

function App() {
  return (
    <EthProvider>
      <div id="App" >
        
          <NavbarNew/>
          
        
      </div>
    </EthProvider>
  );
}
export default App;
