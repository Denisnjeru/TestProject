import api from '../apiV1/api'

const auth = {
  login(content) {
    return new Promise((resolve, reject) => {
      api.post('/auth/token/', content, (data) => {
        resolve(data);
      }, (error) => {
        reject(error);
      });
    });
  },
  signup(content) {
    return new Promise((resolve, reject) => {
      api.post('/auth/signup/', content, (data) => {
        resolve(data);
      }, (error) => {
        reject(error);
      });
    });
  },
  resetPassword(content) {
    return new Promise((resolve, reject) => {
      api.post('/auth/reset_password_request/', content, (data) => {
        resolve(data);
      }, (error) => {
        reject(error);
      });
    });
  },
  setPassword(content) {
    return new Promise((resolve, reject) => {
      api.post('/auth/confirm/', content, (data) => {
        resolve(data);
      }, (error) => {
        reject(error);
      });
    });
  },
}


export default auth