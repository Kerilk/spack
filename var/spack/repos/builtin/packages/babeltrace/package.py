# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Babeltrace(AutotoolsPackage):
    """Babeltrace /ˈbæbəltreɪs/, an EfficiOS project, is an open-source trace manipulation toolkit."""

    homepage = "https://babeltrace.org/"
    url      = "https://www.efficios.com/files/babeltrace/babeltrace-1.5.8.tar.bz2"

    maintainers = ['Kerilk']

    version('1.5.8',      sha256='9ff143e4d1d7f1902b05542ac8f1747fb2d7e0ca31c6fa39ccae5765e11d6fc2')

    variant('python', default=True, description="With python bindings")

    depends_on('elfutils')
    depends_on('popt')
    depends_on('python', when='+python')
    depends_on('swig', when='+python')

    parallel = False

    def configure_args(self):
        args = []
        if '+python' in self.spec:
            args.append('--enable-python-bindings')
        return args
