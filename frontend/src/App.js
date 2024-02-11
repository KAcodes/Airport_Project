import React from "react";
import { BrowserRouter as Router } from "react-router-dom";
import Container from "components/atoms/Container/Container";
import Header from "./components/organisms/Header/Header";
import Navbar from "./components/organisms/Navbar/Navbar";
import { Pages } from "components/routes/routes";

const App = () => {
  return (
    <>
      <Header />
      <Router>
        <Navbar />
        <Container>
          <Pages />
        </Container>
      </Router>
    </>
  );
};

export default App;
