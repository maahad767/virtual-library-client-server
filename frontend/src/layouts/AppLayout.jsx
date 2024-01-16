import { Layout, Menu, theme } from "antd";
const { Header, Content, Footer } = Layout;
import PropTypes from "prop-types";
import { useAuth } from "../hooks/AuthHooks";
import { Link } from "react-router-dom";

const AppLayout = ({ children }) => {
  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken();

  const { user } = useAuth();

  const items = [
    !user && {
      key: "login",
      label: <Link to="/login">Login</Link>,
    },
    !user && {
      key: "register",
      label: "Register",
    },
  ];

  AppLayout.propTypes = {
    children: PropTypes.node,
  };

  return (
    <Layout>
      <Header
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <div className="text-3xl text-white">
          <Link to="/">Community Library</Link>
        </div>
        <div>
          <Menu
            theme="dark"
            mode="horizontal"
            defaultSelectedKeys={["2"]}
            items={items}
            style={{
              flex: 1,
              minWidth: 0,
            }}
          />
        </div>
      </Header>

      <Content
        style={{
          margin: "20px 0px",
          padding: "0 48px",
        }}
      >
        {/* <Breadcrumb
          style={{
            margin: "16px 0",
          }}
        >
          <Breadcrumb.Item>Home</Breadcrumb.Item>
          <Breadcrumb.Item>List</Breadcrumb.Item>
          <Breadcrumb.Item>App</Breadcrumb.Item>
        </Breadcrumb> */}

        <div
          style={{
            background: colorBgContainer,
            minHeight: "75vh",
            padding: 24,
            borderRadius: borderRadiusLG,
          }}
        >
          {children}
        </div>
      </Content>

      <Footer
        style={{
          textAlign: "center",
        }}
      >
        Community Library ©{new Date().getFullYear()} Created by @maahad767
      </Footer>
    </Layout>
  );
};

export default AppLayout;
