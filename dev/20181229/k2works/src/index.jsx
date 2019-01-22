import React from "react";
import ReactDOM from "react-dom";
import {FizzBuzz} from "./components/FizzBuzz";


class App extends React.Component {
  render() {
    return (
      <div>
        <FizzBuzz fizzBuzzUpDownCount={0}/>
      </div>
    );
  }
}

ReactDOM.render(<App/>, document.querySelector("#app"));