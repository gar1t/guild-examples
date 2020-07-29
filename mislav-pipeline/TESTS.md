# Pipeline Example

These tests illustrate the behavior of this sample project.

We run the tests in a separate environment (Guild home directory).

    >>> os.environ["GUILD_HOME"] = mkdtemp()

## Prepare Data

Generate default data set (cats).

    >>> run("guild run prepare-data -y")
    Preparing cats data
    <exit 0>

Generate dogs data set.

    >>> run("guild run prepare-data type=dogs -y")
    Preparing dogs data
    <exit 0>

Use an unsupported type.

    >>> run("guild run prepare-data type=birds -y")
    Unsupported value for 'type' - supported values are:
    <BLANKLINE>
      cats
      dogs
    <BLANKLINE>
    Run the command again using one of these options.
    <exit 1>

Compare  runs.

    >>> run("guild compare -t")
    run  operation     started  time  status     label      type
    ...  prepare-data  ...            completed  type=dogs  dogs
    ...  prepare-data  ...            completed  type=cats  cats
    <exit 0>

## Random Forest

Train a random forest model on the 'cats' data set.

    >>> run("guild run random-forest:train "
    ...     "prepared-data=`guild select -o prepare-data -l cats` -y")
    Resolving prepared-data dependency
    Using run ... for prepared-data resource
    Training random forest model on cats (2 examples)
    acc: 0.9
    <exit 0>

Run attributes show `data_type` as 'cats':

    >>> run("guild runs info")
    id: ...
    operation: random-forest:train
    from: .../mislav-pipeline/guild.yml
    status: completed
    ...
    data_type: cats
    flags:
      prepared-data: ...
    scalars:
      acc: 0.900000 (step 0)
    <exit 0>

Compare runs.

    >>> run("guild compare -t")
    run  operation            started  time  status     label              type  prepared-data  acc       step
    ...  random-forest:train  ...            completed  prepared-data=...  cats  ...            0.899999  0
    ...  prepare-data         ...            completed  type=dogs          dogs
    ...  prepare-data         ...            completed  type=cats          cats
    <exit 0>

## Decision Tree

Train a decision tree model on the 'dogs' data set.

    >>> run("guild run decision-tree:train "
    ...     "prepared-data=`guild select -o prepare-data -l dogs` -y")
    Resolving prepared-data dependency
    Using run ... for prepared-data resource
    Training decision tree model on dogs (3 examples)
    acc: 0.8
    <exit 0>

Run attributes show `data_type` as 'cats':

    >>> run("guild runs info")
    id: ...
    operation: decision-tree:train
    from: .../mislav-pipeline/guild.yml
    status: completed
    ...
    data_type: dogs
    flags:
      prepared-data: ...
    scalars:
      acc: 0.800000 (step 0)
    <exit 0>

Compare runs.

    >>> run("guild compare -t")
    run  operation            started  time  status     label              type  prepared-data  acc       step
    ...  decision-tree:train  ...            completed  prepared-data=...  dogs  ...            0.800000  0
    ...  random-forest:train  ...            completed  prepared-data=...  cats  ...            0.899999  0
    ...  prepare-data         ...            completed  type=dogs          dogs
    ...  prepare-data         ...            completed  type=cats          cats
    <exit 0>