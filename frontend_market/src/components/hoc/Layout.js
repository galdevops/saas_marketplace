import React from "react";
import "css/Layout.css";
import Topbar from "./Topbar";
import Footer from "./Footer";
// https://github.com/Vetrivel-VP/marketplace-dashboard/
function Layout() {
  return (
      <div className="layout">

          <div className="main-wrapper">

              <Topbar />

              <div className="main-content">
                  hi
              </div>
              <Footer />

          </div>
      </div>
  );
}

export default Layout;