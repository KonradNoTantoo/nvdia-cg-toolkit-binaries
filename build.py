from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(docker_32_images=True)
    builder.add_common_builds()
    builder.run()
