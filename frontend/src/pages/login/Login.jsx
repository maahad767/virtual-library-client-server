import { Button, Form, Input, message } from "antd";
import { Navigate, useLocation } from "react-router-dom";
import { useAuth } from "../../hooks/AuthHooks";
import { AccountService } from "../../services/AccountService";

const Login = () => {
  const { login, isAuthenticated } = useAuth();
  const location = useLocation();

  if (isAuthenticated) {
    return <Navigate to="/" replace state={{ from: location }} />;
  }

  const onFinish = async (values) => {
    console.log("Success:", values);

    try {
      const resp = await AccountService.getToken(
        values.username,
        values.password
      );
      message.success("Login Successful");
      console.log(
        "access, refresh, user: ",
        resp.data.access_token,
        resp.data.refresh_token,
        resp.data.user
      );
      login(resp.data.access_token, resp.data.refresh_token, resp.data.user);
    } catch (error) {
      console.error("An error occurred: ", error.message);
      message.error({
        content: error.message,
      });
    }
  };

  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };

  return (
    <>
      <h1 className="text-4xl text-center mb-10">Login</h1>
      <Form
        name="login"
        style={{
          maxWidth: 600,
          margin: "auto auto",
        }}
        initialValues={{
          remember: true,
        }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
        autoComplete="off"
        size="large"
      >
        <Form.Item
          label="Username"
          name="username"
          rules={[
            {
              required: true,
              message: "Please input your username!",
            },
          ]}
        >
          <Input />
        </Form.Item>

        <Form.Item
          label="Password"
          name="password"
          rules={[
            {
              required: true,
              message: "Please input your password!",
            },
          ]}
        >
          <Input.Password />
        </Form.Item>

        <Form.Item>
          <Button
            type="primary"
            className="bg-blue-700 text-white"
            style={{
              width: "100%",
              height: "40px",
            }}
            htmlType="submit"
          >
            Login
          </Button>
        </Form.Item>
      </Form>
    </>
  );
};
export default Login;
