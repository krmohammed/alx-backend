import redis from 'redis';

const redisCli = redis.createClient();

redisCli.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

redisCli.on('connect', () => {
  console.log('Redis client connected to the server');
});
