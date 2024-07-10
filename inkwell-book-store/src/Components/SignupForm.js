import React from 'react';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import './LoginForm.css';

const SignupSchema = Yup.object().shape({
  username: Yup.string().required('Required'),
  email: Yup.string().email('Invalid email').required('Required'),
  password: Yup.string().required('Required'),
});

const SignupForm = () => (
  <Formik
    initialValues={{ username: '', email: '', password: '' }}
    validationSchema={SignupSchema}
    onSubmit={(values, { setSubmitting }) => {
      fetch('/api/users', {
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
        .catch(error => console.error('There was an error signing up!', error));
    }}
  >
    {({ isSubmitting }) => (
      <div className="form-container">
        <Form>
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <Field type="text" name="username" placeholder="Username" />
            <ErrorMessage name="username" component="div" className="error" />
          </div>
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
          <button type="submit" disabled={isSubmitting}>Sign Up</button>
        </Form>
      </div>
    )}
  </Formik>
);

export default SignupForm;
