import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import './LoginForm.css';

const LoginSchema = Yup.object().shape({
  email: Yup.string().email('Invalid email').required('Required'),
  password: Yup.string().required('Required'),
});

const LoginForm = () => (
  <Formik
    initialValues={{ email: '', password: '' }}
    validationSchema={LoginSchema}
    onSubmit={(values, { setSubmitting }) => {
      fetch('/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
      }).then(response => response.json())
        .then(data => {
          console.log(data);
          setSubmitting(false);
        })
        .catch(error => console.error('There was an error logging in!', error));
    }}
  >
    {({ isSubmitting }) => (
      <div className="form-container">
        <Form>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <Field type="email" name="email" placeholder="Email" />
            <ErrorMessage name="email" component="div" className="error" />
          </div>
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <Field type="password" name="password" placeholder="Password" />
            <ErrorMessage name="password" component="div" className="error" />
          </div>
          <button type="submit" disabled={isSubmitting}>Log In</button>
        </Form>
      </div>
    )}
  </Formik>
);

export default LoginForm;

