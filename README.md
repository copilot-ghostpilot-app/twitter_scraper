# copilot-spooktacular-tweet-scraper

#### Getting started

1. Create a Twitter "App" and generate secrets in the [developer console](https://developer.twitter.com/en).
2. Once you have the secrets, create the secret ssm parameters (for reference, see [copilot secrets](https://aws.github.io/copilot-cli/docs/developing/secrets/)):
  ```bash
  # Make sure the tag values match your environment and application
  aws ssm put-parameter --name TWITTER_ACCESS_TOKEN --value "VALUEHERE" --type SecureString --tags Key=copilot-environment,Value=test Key=copilot-application,Value=spooky-demo
  aws ssm put-parameter --name TWITTER_ACCESS_TOKEN_SECRET --value "VALUEHERE" --type SecureString --tags Key=copilot-environment,Value=test Key=copilot-application,Value=spooky-demo
  aws ssm put-parameter --name TWITTER_CONSUMER_API_KEY --value "VALUEHERE" --type SecureString --tags Key=copilot-environment,Value=test Key=copilot-application,Value=spooky-demo
  aws ssm put-parameter --name TWITTER_CONSUMER_API_SECRET --value "VALUEHERE" --type SecureString --tags Key=copilot-environment,Value=test Key=copilot-application,Value=spooky-demo
  ```
3. The manifest file already has the required environment variables and secrets set. Simply deploy the job!
  ```bash
  copilot job deploy --name twitter-scraper --env test
  ```
