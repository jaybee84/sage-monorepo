# Develop on a remote host

## Introduction

Team members who develop locally may not benefit from the same compute resources. The most notable
resources that can impact the productivity of developers are the number and frequency of the CPU
cores, the memory available and internet speed. The worse case is when a machine does not have the
resources to run the apps that the team develops, for example when not enough memory is available.
On other times, the time required to complete a task may be many times slower on a computer with
lower CPU resources.

Working remotely means that developers no longer benefit from the same internet speed, either
because of the quality of the internet connection available at their location or because the speed
is shared among the members of a household. As a result, tasks that involve downloading or uploading
artifacts, like pulling or pushing Docker images, may take significantly longer to complete.

This page describes how to setup a development environment that enables developers to use VS Code
while using the compute resources of a remote host. The developers start by creating identical EC2
instances before [connecting to them with VS
Code](https://code.visualstudio.com/remote/advancedcontainers/develop-remote-host). This SOP enables
developers to continue working [inside the devcontainer](#devcontainer) provided with this project,
hence further contributing to the standardization of the development envrionment.

> **Note** 2023-01-28: Added documentation to connect to a GitHub Codespace.

## Use case

This table summarizes the local compute resources available to the developers of the challenge
registry. The same information is displayed for two types of Amazon EC2 instances and one type of
GitHub Codespace instance that were selected as candidate alternative development environments for
the team members. The table also includes the runtimes in seconds of different tasks such as linting
or testing all the projects included in the monorepo (the method used to generate these results is
described in the next section).

|                                                        | Shirou       | Rin          | Sakura       | m5.2xlarge   | t3a.xlarge   | 4-core Codespace | 8-core Codespace |
| ------------------------------------------------------ | ------------ | ------------ | ------------ | ------------ | ------------ | ---------------- | ---------------- |
| Computer Type                                          | Desktop PC   | MacBook Pro  | MacBook Pro  | Amazon EC2   | Amazon EC2   | GitHub Codespace | GitHub Codespace |
| Architecture                                           | 64-bit (x86) | 64-bit (x86) | 64-bit (x86) | 64-bit (x86) | 64-bit (x86) | 64-bit (x86)     | 64-bit (x86)     |
| CPU Count                                              | 8            | 4            | 4            | 8            | 4            | 4                | 8                |
| CPU Frequency (GHz)                                    | 3.6          | 2.4          | 1.7          | 2.5          | 2.2          | 2.7              | 2.8              |
| Memory (GB)                                            | 32           | 16           | 16           | 32           | 16           | 8                | 16               |
| Runtime: Lint All Projects (s)                         | 15.4         | 208.9        | 183.8        | 18.6         | 33.4         | 24.6             | 16.9             |
| Runtime: Build All Projects (s)                        | 19.4         | 196.2        | 162.2        | 26.7         | 44.9         | 32.3             | 14.1             |
| Runtime: Test All Projects (s)                         | 12.4         | 117.1        | 82.8         | 15.3         | 29.2         | 31.6             | 24.5             |
| Runtime: Test api (s)                                  | 6.2          | 29.6         | 21.3         | 7.2          | 10.4         | 6.5              | 6.5              |
| Runtime: Test web-app (s)                              | 5.3          | 43.0         | 35.0         | 6.5          | 9.2          | 6.7              | 6.0              |
| Download speed (Mbit/s)                                | 395.9        | 52.1         | 160.1        | 2165.0       | 1606.7       | 8571             | 8603             |
| Upload speed (Mbit/s)                                  | 183.3        | 15.6         | 10.3         | 1861.0       | 1030.2       | 4893             | 5125             |
| On-Demand Cost ($/day)                                 | n/a          | n/a          | n/a          | 9.2          | 3.6          | 8.64 (1,2)       | 17.28 (1,2)      |
| On-Demand Cost ($/year)                                | n/a          | n/a          | n/a          | 3363.8       | 1317.5       | 3153.6 (1,2)     | 6307.2 (1,2)     |

(1) GitHub codespaces stop automatically after 1h of inactivity. A codespace used by an engineer
with 100 %FTE and 8 working hours per day - without taking into account vacation for the sake of
simplicity - would cost 8 hours/day * 5 days/week * 52 weeks * $0.36/hour (4-core) = $748/year (see
[Codespaces pricing]). Similarly, the cost for an 8-core codespace would become $1496/year. In
addition, GitHub bills $0.07 of GB of storage.

(2) GitHub offers core hours and storage. For example, a Free user can use a 2-core instance for 60
hours per month for free or an 8-core instance for 15 hours. You will be notified by email when you
have used 75%, 90%, and 100% of your included quotas.
  - Free users: 120 core hours/month and 15 GB month of storage
  - Pro users: 180 core hours/month and 20 GB month of storage

Note that developers have been asked to measure runtimes and internet speeds while keeping open the
applications that are usually running when they develop (e.g. Spotify, several instances of VS Code,
browser with many tabs open). This could be one reason why runtimes reported by a developer are
larger that those reported by another developer who has less compute resources available.

The table below shows the number of times a task is faster than the slowest runtime (denoted by
"1.0").

|                                                        | Shirou       | Rin          | Sakura       | m5.2xlarge   | t3a.xlarge   |
| ------------------------------------------------------ | ------------ | ------------ | ------------ | ------------ | ------------ |
| Runtime: Lint All Projects                             | 13.6         | 1.0          | 1.1          | 11.2         | 6.3          |
| Runtime: Build All Projects                            | 10.1         | 1.0          | 1.2          | 7.3          | 4.4          |
| Runtime: Test All Projects                             | 9.4          | 1.0          | 1.4          | 7.6          | 4.0          |
| Runtime: Test api                                      | 4.8          | 1.0          | 1.4          | 4.1          | 2.8          |
| Runtime: Test web-app                                  | 8.0          | 1.0          | 1.2          | 6.6          | 4.6          |
| Download speed                                         | 7.6          | 1.0          | 3.1          | 41.5         | 30.8         |
| Upload speed                                           | 17.8         | 1.5          | 1.0          | 180.5        | 99.9         |

For example, linting all the projects of this monorepo is 13.6 times faster on Shirou's computer
than on Rin's. Moreover, all the developers can benefit from improved download speeds (up to 41.5
faster for Rin) and upload speeds (up to 180.5 times faster for Sakura) when developing on an EC2
instance. This table illustrates well the diversity in compute resources available locally to
developers, and how relying on remote hosts like EC2 instances can provide a better working
environment to developers.

### Data collection

- Runtimes are obtained from [this
  commit](https://github.com/Sage-Bionetworks/sage-monorepo/tree/25f2292388d9e71bf46ba137aa530aefb571deab).
- Identification of the compute resources.
  ```console
  $ nproc
  $ cat /proc/cpuinfo
  $ cat /proc/meminfo
  ```
- Runtimes are averaged over 10 runs that follow a warmup run using
  [hyperfine](https://github.com/sharkdp/hyperfine).
  ```console
  $ hyperfine --warmup 1 --runs 10 'nx run-many --all --target=lint --skip-nx-cache'
  $ hyperfine --warmup 1 --runs 10 'nx run-many --all --target=build --skip-nx-cache'
  $ hyperfine --warmup 1 --runs 10 'nx run-many --all --target=test --skip-nx-cache'
  $ hyperfine --warmup 1 --runs 10 'nx test api --skip-nx-cache'
  $ hyperfine --warmup 1 --runs 10 'nx test web-ui --skip-nx-cache'
  ```
- Internet speeds are measured with [speedtest-cli](https://www.speedtest.net/apps/cli).
  ```console
  $ speedtest
  ```

## Preparing the remote host (AWS EC2)

This section describes how to instantiate an AWS EC2 as the remote host.  Steps outlined below will
assume you have access to the Sage AWS Service Catalog.

### On the Service Catalog Portal

- Log in to the [Service Catalog](https://sc.sageit.org) with your Synapse credentials.
- From the list of Products, select **EC2: Linux Docker**. On the Product page, click on **Launch
product** in the upper-right corner.
- On the next page, fill out the wizard as follows:
  - **Provisioned product name**
    - Name: `<GitHub username>-devcontainers`
  - **Parameters**:
    - EC2 Instance Type: `t3.2xlarge`
    - Base Image: `AmazonLinuxDocker` (leave default)
    - Disk Size: 80
  - **Manage tags**:
    - `Department`: `IBC` or `CNB` (selected from [this
      list](https://github.com/Sage-Bionetworks-IT/organizations-infra/blob/master/sceptre/scipool/sc-tag-options/internal/Departments.json))
    - `Project`: `challenge` (selected from [this
      list](https://github.com/Sage-Bionetworks-IT/organizations-infra/blob/master/sceptre/scipool/sc-tag-options/internal/Projects.json))
    - `CostCenter`: `NIH-ITCR / 101600` (selected from [these
      lists](https://github.com/Sage-Bionetworks/aws-infra/tree/master/templates/tags))
  - **Enable event notifications**: SKIP - DO NOT MODIFY
- Click on **Launch product**. Your instance will take anywhere between 3-5 minutes to deploy.  You
can either wait on this page until "EC2Instance" shows up on the list under Resources, or you can
leave and come back at a later time.

### On your local host

> #### Note:
> If this is your first time **ever** connecting to an instance from your machine, you will first
> need to set up EC2 access with the AWS Systems Manager (SSM). Follow the instructions below to
> complete the setup:
>  - [**Create a Synapse personal access
>    token**](https://help.sc.sageit.org/sc/Service-Catalog-Provisioning.938836322.html#ServiceCatalogProvisioning-CreateaSynapsepersonalaccesstoken)
>  - [**SSM access to an
>    Instance**](https://help.sc.sageit.org/sc/Service-Catalog-Provisioning.938836322.html#ServiceCatalogProvisioning-SSMaccesstoanInstance)
>
> (Don't worry, you will only need to do this once for your local machine!)

- In your terminal, connect to your instance following the [**Connecting to an Instance - SSM with
SSH**](https://help.sc.sageit.org/sc/Service-Catalog-Provisioning.938836322.html#ServiceCatalogProvisioning-SSMwithSSH)
instructions from the Service Catalog Provisioning doc.
- Once you can successfully login through SSM with SSH, exit the instance.
- Navigate to the Provisioned products page for your instance.  Under **Events**, copy the
`EC2InstancePrivateIpAddress`
- In your terminal, add the following into your local `~/.ssh/config`:
   ```console
   Host devcontainers
       HostName <private_ip>
       User ec2-user
       IdentityFile ~/.ssh/id_rsa
   ```
- Connect to the [Sage
  VPN](https://sagebionetworks.jira.com/wiki/spaces/IT/pages/1705246745/AWS+Client+VPN+User+Guide)
- In your terminal, SSH to the instance to ensure `~/.ssh/config` was setup correctly.
   ```console
   ssh devcontainers
   ```

### On the EC2 instance

- Update the system packages.
   ```console
   sudo yum update -y
   ```
- Docker should already be readily available on the instance. Verify this by running any Docker
command, e.g.
   ```console
   docker --version
   ```
- Clone your fork into the home directory.
- To easily pull and push changes, we suggest storing your GitHub credentials onto the instance.
Follow the [**Storing GitHub credentials on the EC2
instance**](https://sagebionetworks.jira.com/wiki/spaces/APGD/pages/2590244872/Service+Catalog+Instance+Setup#Storing-GitHub-credentials-on-the-EC2-instance).
instructions to do so.

### In VS Code

- Install the extension `Remote - SSH` and `Remote - Containers`.
- `Remote-SSH: Connect to Host...` > Select the host.
- Verify that the bottom-left corner of the VSCode window shows `SSH: <host name>` upon successfully
  connecting to the remote instance.

  <img src="images/vscode-remote-ssh-button.png" height="24">

- `Remote-Containers: Open Folder in Container...`
- Select the project folder and click on `OK`.
- Verify that the bottom-left corner of the VSCode window shows `Dev Container: OpenChallenges @
  ssh://<host name>`.

  <img src="images/vscode-remote-ssh-devcontainer-button.png" height="58">

Congratulations, you are now ready to develop in the devcontainer that runs on the EC2 instance! 🚀

## Preparing the remote host (GitHub Codespace)

1. Open your browser and go to [GitHub Codespaces].
2. Click on the "New codespace".
3. Enter the information requested:
    - `Repository`: Select your fork of the monorepo
    - `Branch`: Select the default branch
    - `Dev container configuration`: Select the dev container definition
    - `Region`: Select your preferred region
    - `Machine type`: Select the machine type
        > **Note** 4-core is preferred for the OpenChallenges project as a trade-off between
        > performance and cost.
4. Click on "Create codespace".
5. Wait for the codespace to be created.
6. Configure the monorepo and install its dependencies (see README).

### Stopping a Codespace instance

If your codespace is open in your browser, you can stop it with the following step. Note that a
codespace stops automatically after one hour of inactivity.

1. Click on the button "Codespaces" located in the bottom-left corner.
2. Click on "Stop Current Codespace".

### Opening a Codespace with VS Code

If you prefer to develop with VS Code rather than inside your browser:

1. Open your browser and go to [GitHub Codespaces].
2. Find the codespace that you want to open with VS Code.
3. Click on the three-dot menu > "Open in ..." > "Open in Visual Studio Code"

### Changing the machine type

The type of machine used by a codespace can be changed at any time, for example when a beefier
codespace instance is needed. To change the machine type of an existing codespace.

1. Stop the codespace.
2. Open your browser and go to [GitHub Codespaces].
3. Find the codespace that you want to open with VS Code.
4. Click on the three-dot menu > "Change machine type".
5. Update the properties of the machine and click on "Update codespace".

## Accessing apps and services

The devcontainer provided with this project uses the VS Code devcontainer feature
`docker-in-docker`. In addition to isolating the Docker engine running in the devcontainer from the
engine running on the host, this feature enables VS Code to forward the ports defined in
`devcontainer.json` to the local envrionment of the developer. Therefore, apps and services can be
accessed using the address `http://localhost` even though they are running on the remote host!

Accessing the apps and services using the IP address of the remote host won't work, unless you
replace the feature `docker-in-docker` by `docker-from-docker`. In this case, `http://localhost` can
no longer be used to access the apps and services.

## Uploading files

Simply drag and drop files to the VS Code explorer to upload files from your local environment to
the remote host.

## Closing the remote connection

Click on the button in the bottom-left corner of VS Code and select one of these options:

- `Close Remote Connection` to close the connection with the remote host.
- `Reopen Folder in SSH` if you want to stop the devcontainer but stay connected to the remote host.

<!-- Links -->

[GitHub Codespaces]: https://github.com/codespaces
[Codespaces pricing]: https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces