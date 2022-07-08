import api from '../apiV1/api';

const user = {
  userProfile(userId) {
    return new Promise((resolve, reject) => {
      api.get(`/auth/profile/${userId}/`, (data) => {
        resolve(data);
      }, (error) => {
        reject(error);
      });
    });
  },
  createUser(content) {
    return new Promise((resolve, reject) => {
      api.post('/company/allusers/', content, (data) => {
        resolve(data);
      }, (error) => {
        reject(error);
      });
    });
  },
};

export default user;